// Auto-generated. Do not edit!

// (in-package humanoid_nav_msgs.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let StepTarget = require('./StepTarget.js');

//-----------------------------------------------------------

class ExecFootstepsFeedback {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.executed_footsteps = null;
    }
    else {
      if (initObj.hasOwnProperty('executed_footsteps')) {
        this.executed_footsteps = initObj.executed_footsteps
      }
      else {
        this.executed_footsteps = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type ExecFootstepsFeedback
    // Serialize message field [executed_footsteps]
    // Serialize the length for message field [executed_footsteps]
    bufferOffset = _serializer.uint32(obj.executed_footsteps.length, buffer, bufferOffset);
    obj.executed_footsteps.forEach((val) => {
      bufferOffset = StepTarget.serialize(val, buffer, bufferOffset);
    });
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type ExecFootstepsFeedback
    let len;
    let data = new ExecFootstepsFeedback(null);
    // Deserialize message field [executed_footsteps]
    // Deserialize array length for message field [executed_footsteps]
    len = _deserializer.uint32(buffer, bufferOffset);
    data.executed_footsteps = new Array(len);
    for (let i = 0; i < len; ++i) {
      data.executed_footsteps[i] = StepTarget.deserialize(buffer, bufferOffset)
    }
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += 25 * object.executed_footsteps.length;
    return length + 4;
  }

  static datatype() {
    // Returns string type for a message object
    return 'humanoid_nav_msgs/ExecFootstepsFeedback';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '5dfde2cb244d6c76567d3c52c40a988c';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    # ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======
    # Define a feedback message
    humanoid_nav_msgs/StepTarget[] executed_footsteps
    
    
    ================================================================================
    MSG: humanoid_nav_msgs/StepTarget
    # Target for a single stepping motion of a humanoid's leg
    
    geometry_msgs/Pose2D pose   # step pose as relative offset to last leg
    uint8 leg                   # which leg to use (left/right, see below)
    
    uint8 right=0               # right leg constant
    uint8 left=1                # left leg constant
    
    ================================================================================
    MSG: geometry_msgs/Pose2D
    # This expresses a position and orientation on a 2D manifold.
    
    float64 x
    float64 y
    float64 theta
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new ExecFootstepsFeedback(null);
    if (msg.executed_footsteps !== undefined) {
      resolved.executed_footsteps = new Array(msg.executed_footsteps.length);
      for (let i = 0; i < resolved.executed_footsteps.length; ++i) {
        resolved.executed_footsteps[i] = StepTarget.Resolve(msg.executed_footsteps[i]);
      }
    }
    else {
      resolved.executed_footsteps = []
    }

    return resolved;
    }
};

module.exports = ExecFootstepsFeedback;
