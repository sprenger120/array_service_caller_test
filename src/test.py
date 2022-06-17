#!/usr/bin/env python3

from array_service_caller_test.srv import ArraySrv, ArraySrvResponse, ArraySrvRequest
import rospy


def serviceRequest(req: ArraySrvRequest):
    print(req)
    return ArraySrvResponse()



if __name__ == "__main__":
    rospy.init_node('array_service_test', anonymous=False)
    rospy.Service('array_service_test', ArraySrv, serviceRequest)
    print("Ready.")
    rospy.spin()