; Auto-generated. Do not edit!


(cl:in-package asv-msg)


;//! \htmlinclude propd.msg.html

(cl:defclass <propd> (roslisp-msg-protocol:ros-message)
  ((prop_demand
    :reader prop_demand
    :initarg :prop_demand
    :type cl:float
    :initform 0.0))
)

(cl:defclass propd (<propd>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <propd>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'propd)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name asv-msg:<propd> is deprecated: use asv-msg:propd instead.")))

(cl:ensure-generic-function 'prop_demand-val :lambda-list '(m))
(cl:defmethod prop_demand-val ((m <propd>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader asv-msg:prop_demand-val is deprecated.  Use asv-msg:prop_demand instead.")
  (prop_demand m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <propd>) ostream)
  "Serializes a message object of type '<propd>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'prop_demand))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <propd>) istream)
  "Deserializes a message object of type '<propd>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'prop_demand) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<propd>)))
  "Returns string type for a message object of type '<propd>"
  "asv/propd")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'propd)))
  "Returns string type for a message object of type 'propd"
  "asv/propd")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<propd>)))
  "Returns md5sum for a message object of type '<propd>"
  "b80390de6505fc9f662044172e64f5d7")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'propd)))
  "Returns md5sum for a message object of type 'propd"
  "b80390de6505fc9f662044172e64f5d7")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<propd>)))
  "Returns full string definition for message of type '<propd>"
  (cl:format cl:nil "float32 prop_demand~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'propd)))
  "Returns full string definition for message of type 'propd"
  (cl:format cl:nil "float32 prop_demand~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <propd>))
  (cl:+ 0
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <propd>))
  "Converts a ROS message object to a list"
  (cl:list 'propd
    (cl:cons ':prop_demand (prop_demand msg))
))
