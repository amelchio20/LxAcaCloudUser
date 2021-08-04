import boto3
import datetime
# import pytz

ec2 = boto3.resource('ec2')

def lambda_handler(event, context):
    instances = ec2.instances.filter(
        Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
    
    for instance in instances:
        # diese zeile arbeitet so NICHT
        # instance_name = filter(lambda tag: tag['Key'] == 'Name', instance.tags)[0]['Value']

        # ERSETZEN DURCH
        for tag in instance.tags:
          if tag["Key"] == 'Name':
            instance_name = tag["Value"]
        
        for volume in ec2.volumes.filter(Filters=[{'Name': 'attachment.instance-id', 'Values': [instance.id]}]):
            description = 'scheduled-%s.%s-%s' % (instance_name, volume.volume_id, 
                datetime.datetime.now().strftime("%Y%m%d-%H%M%S"))
                
        if volume.create_snapshot(VolumeId=volume.volume_id, Description=description):
            print("Snapshot created with description [%s]" % description)

        for snapshot in volume.snapshots.all():
            retention_days = 15
            if snapshot.description.startswith('scheduled-') and ( datetime.datetime.now().replace(tzinfo=None) - snapshot.start_time.replace(tzinfo=None) ) > datetime.timedelta(days=retention_days):
                print("\t\tDeleting snapshot [%s - %s]" % ( snapshot.snapshot_id, snapshot.description ))
                snapshot.delete()

    return True
