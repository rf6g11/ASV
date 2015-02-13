; Auto-generated. Do not edit!


(cl:in-package asv-msg)


;//! \htmlinclude rudderd.msg.html

(cl:defclass <rudderd> (roslisp-msg-protocol:ros-message)
  ((rudder_demand
    :reader rudder_demand
    :initarg :rudder_demand
    :type cl:float
    :initform 0.0))
)

(cl:defclass rudderd (<rudderd>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <rudderd>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'rudderd)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name asv-msg:<rudderd> is deprecated: use asv-msg:rudderd instead.")))

(cl:ensure-generic-function 'rudder_demand-val :lambda-list '(m))
(cl:defmethod rudder_demand-val ((m <rudderd>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader asv-msg:rudder_demand-val is deprecated.  Use asv-msg:rudder_demand instead.")
  (rudder_demand m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <rudderd>) ostream)
  "Serializes a message object of type '<rudderd>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'rudder_demand))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <rudderd>) istream)
  "Deserializes a message object of type '<rudderd>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'rudder_demand) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<rudderd>)))
  "Returns string type for a message object of type '<rudderd>"
  "asv/rudderd")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'rudderd)))
  "Returns string type for a message object of type 'rudderd"
  "asv/rudderd")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<rudderd>)))
  "Returns md5sum for a message object of type '<rudderd>"
  "60078da9d4c3d9307b5235a0a0d7c95a")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'rudderd)))
  "Returns md5sum for a message object of type 'rudderd"
  "60078da9d4c3d9307b5235a0a0d7c95a")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<rudderd>)))
  "Returns full string definition for message of type '<rudderd>"
  (cl:format cl:nil "float32 rudder_demand~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'rudderd)))
  "Returns full string definition for message of type 'rudderd"
  (cl:format cl:nil "float32 rudder_demand~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <rudderd>))
  (cl:+ 0
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <rudderd>))
  "Converts a ROS message object to a list"
  (cl:list 'rudderd
    (cl:cons ':rudder_demand (rudder_demand msg))
))
