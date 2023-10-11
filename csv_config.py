import yaml
import numpy
# Open the metrics configuration file metrics.yml and retrieve settings
with open("MetricsConfig.yml", 'r') as f:
    metrics = yaml.load(f, Loader=yaml.FullLoader)


def csv_header():
    csv_headers = [
        'Name',
        'Instance',
        'Image Id'
        'Public Ip'
        'Type',
        'Hypervisor',
        'Virtualization Type',
        'Architecture',
        'EBS Optimized']
    for metric in metrics['metrics']:
        csv_headers.append(metric['name'] + " (" + metric['unit'] + ")")
    return csv_headers


def write_csv(csvwriter, resource, metrics_info):
    name_dict = None
    if resource.tags:
        name_dict = next(
            (i for i in resource.tags if i['Key'] == 'Name'),
            None)
    csvwriter.writerow([
        '' if name_dict is None else name_dict.get('Value'),
        resource.id,
        resource.image_id,
        resource.public_ip_address,
        resource.instance_type,
        resource.hypervisor,
        resource.virtualization_type,
        resource.architecture,
        resource.ebs_optimized,
        numpy.round(numpy.average(metrics_info['CPUUtilization']), 2),
        numpy.round(numpy.average(metrics_info['DiskReadOps']), 2),
        numpy.round(numpy.average(metrics_info['DiskReadBytes']), 2),
        numpy.round(numpy.average(metrics_info['DiskWriteBytes']), 2),
        numpy.round(numpy.average(metrics_info['NetworkIn']), 2),
        numpy.round(numpy.average(metrics_info['NetworkOut']), 2),
        numpy.round(numpy.average(metrics_info['NetworkPacketsIn']), 2),
        numpy.round(numpy.average(metrics_info['NetworkPacketsOut']), 2)
    ])


