import boto3
import datetime
import yaml
import csv
from csv_config import write_csv, csv_header

session = boto3.session.Session(region_name='us-east-2')
client = session.client('cloudwatch')
ec2 = session.resource('ec2')

now = datetime.datetime.now()

# Open the metrics configuration file metrics.yaml and retrive settings
with open("MetricsConfig.yml", 'r') as f:
    metrics = yaml.load(f, Loader=yaml.FullLoader)


def get_resource():
    return ec2.instances.filter(
                Filters=[
                    {'Name': 'instance-state-name', 'Values': ['running']}])


def get_metrics(id_):
    data_points = {}
    for metric in metrics['metrics']:
        result = client.get_metric_statistics(
                    Namespace="AWS/EC2",
                    MetricName=metric['name'],
                    Dimensions=[{
                        'Name': 'InstanceId',
                        'Value': id_
                    }],
                    Unit=metric['unit'],
                    Period=300,
                    StartTime=now - datetime.timedelta(hours=24),
                    EndTime=now,
                    Statistics=['Maximum']
            )
        actual_datapoint = []
        for datapoint in result['Datapoints']:
            actual_datapoint.append(datapoint['Maximum'])
        data_points[metric['name']] = actual_datapoint
    return data_points


if __name__ == '__main__':

    resource = next(iter(get_resource()))
    data_points_ = get_metrics(id_=resource.id)
    # print(data_points_)

    filename = 'ec2'+".csv"
    with open(filename, 'w') as csvfile:
        # initialize csv writer
        csvwriter = csv.writer(
            csvfile,
            delimiter=',',
            quotechar='"',
            quoting=csv.QUOTE_MINIMAL)

        # write the headers to csv
        csv_headers = csv_header()
        csvwriter.writerow(csv_headers)

        write_csv(csvwriter, resource=resource, metrics_info=data_points_)
        print('CSV file created successfully !!!')
