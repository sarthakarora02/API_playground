### Code referenced from Google Cloud Video Intelligence API doc
### https://cloud.google.com/video-intelligence/docs/label-tutorial
import os
from google.cloud import videointelligence

def analyse (path):
    os.chdir(path)
    os.chdir("../")
    """Detect labels given a file path."""
    video_client = videointelligence.VideoIntelligenceServiceClient()
    features = [videointelligence.enums.Feature.LABEL_DETECTION]

    with open('./twitter_images/vid.mp4', 'rb') as movie:
        input_content = movie.read()

    mode = videointelligence.enums.LabelDetectionMode.SHOT_AND_FRAME_MODE
    config = videointelligence.types.LabelDetectionConfig(label_detection_mode=mode)
    context = videointelligence.types.VideoContext(label_detection_config=config)

    operation = video_client.annotate_video(
        features=features, input_content=input_content, video_context=context)
    print('\nProcessing video for label annotations:')
    print('Please wait...')

    result = operation.result(timeout=90)
    print('\nFinished processing.')

    # Process frame level label annotations
    frame_labels = result.annotation_results[0].frame_label_annotations
    for i, frame_label in enumerate(frame_labels):
        #print('Frame label description: {}'.format(frame_label.entity.description))
        print('Frame label description: ' + frame_label.entity.description.encode('utf-8'))
        for category_entity in frame_label.category_entities:
            print('\tLabel category description: {}'.format(category_entity.description))

        # Each frame_label_annotation has many frames,
        a=0
        for frame in frame_label.frames:
            time_offset = (frame.time_offset.seconds +
                           frame.time_offset.nanos / 1e9)
            print('\tframe time offset: {}s'.format(time_offset))
            print('\tframe confidence: {}'.format(frame.confidence))
            print('\n')
            a+=1
