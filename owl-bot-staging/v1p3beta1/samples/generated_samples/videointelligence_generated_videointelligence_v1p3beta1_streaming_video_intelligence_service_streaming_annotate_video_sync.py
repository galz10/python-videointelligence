# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Generated code. DO NOT EDIT!
#
# Snippet for StreamingAnnotateVideo
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-videointelligence


# [START videointelligence_generated_videointelligence_v1p3beta1_StreamingVideoIntelligenceService_StreamingAnnotateVideo_sync]
from google.cloud import videointelligence_v1p3beta1


def sample_streaming_annotate_video():
    # Create a client
    client = videointelligence_v1p3beta1.StreamingVideoIntelligenceServiceClient()

    # Initialize request argument(s)
    request = videointelligence_v1p3beta1.StreamingAnnotateVideoRequest(
    )

    # This method expects an iterator which contains
    # 'videointelligence_v1p3beta1.StreamingAnnotateVideoRequest' objects
    # Here we create a generator that yields a single `request` for
    # demonstrative purposes.
    requests = [request]
    def request_generator():
        for request in requests:
            yield request

    # Make the request
    stream = client.streaming_annotate_video(requests=request_generator())
    for response in stream:
        print(response)

# [END videointelligence_generated_videointelligence_v1p3beta1_StreamingVideoIntelligenceService_StreamingAnnotateVideo_sync]
