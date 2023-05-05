import pika, json

def upload(f, fs, channel, access):
    '''
    -- upload the file to the mongodb database using gridfs
    -- once the file is uploaded, put a message in the rabbitmq queue
    -- so that a downstream service can process the upload 
    -- Asynchronous communication flow between gateway service and file processing service

    Parameters:
        f (file): file content to be uploaded
        fs (gridfs.GridFS): GridFS object
        channel (pika.channel.Channel): rabbitMq channel
        access (dict): jwt access token

    Returns:
        tuple or None: an error message if an error occured

    '''
        




    '''If file is uploaded successfully mongodb will return a file Id'''
    try:
        fid = fs.put(f)
    except Exception as err:
        return "internal server error", 500





    '''
    The message object that will be pushed into the rabbitMQ queue
    to be consumed by our file processing service
    '''
    message = {
        "video_fid": str(fid),
        "mp3_fid": None,
        "username": access["username"],
    }

    try:
        channel.basic_publish(
            exchange="", # default
            routing_key="video", # name of the rabbitMQ queue
            body=json.dumps(message) # converts python object to json string
            properties=pika.BasicProperties(
                delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
            )
        )
    except:
        fs.delete(fid)
        return "internal server error", 500