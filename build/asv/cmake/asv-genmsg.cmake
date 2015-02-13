# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "asv: 8 messages, 0 services")

set(MSG_I_FLAGS "-Iasv:/home/ric_94/catkin_ws/src/asv/msg;-Istd_msgs:/opt/ros/indigo/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(genlisp REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(asv_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/ric_94/catkin_ws/src/asv/msg/compass.msg" NAME_WE)
add_custom_target(_asv_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "asv" "/home/ric_94/catkin_ws/src/asv/msg/compass.msg" ""
)

get_filename_component(_filename "/home/ric_94/catkin_ws/src/asv/msg/status.msg" NAME_WE)
add_custom_target(_asv_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "asv" "/home/ric_94/catkin_ws/src/asv/msg/status.msg" ""
)

get_filename_component(_filename "/home/ric_94/catkin_ws/src/asv/msg/gps.msg" NAME_WE)
add_custom_target(_asv_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "asv" "/home/ric_94/catkin_ws/src/asv/msg/gps.msg" ""
)

get_filename_component(_filename "/home/ric_94/catkin_ws/src/asv/msg/propd.msg" NAME_WE)
add_custom_target(_asv_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "asv" "/home/ric_94/catkin_ws/src/asv/msg/propd.msg" ""
)

get_filename_component(_filename "/home/ric_94/catkin_ws/src/asv/msg/arduino.msg" NAME_WE)
add_custom_target(_asv_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "asv" "/home/ric_94/catkin_ws/src/asv/msg/arduino.msg" ""
)

get_filename_component(_filename "/home/ric_94/catkin_ws/src/asv/msg/position.msg" NAME_WE)
add_custom_target(_asv_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "asv" "/home/ric_94/catkin_ws/src/asv/msg/position.msg" ""
)

get_filename_component(_filename "/home/ric_94/catkin_ws/src/asv/msg/headingd.msg" NAME_WE)
add_custom_target(_asv_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "asv" "/home/ric_94/catkin_ws/src/asv/msg/headingd.msg" ""
)

get_filename_component(_filename "/home/ric_94/catkin_ws/src/asv/msg/rudderd.msg" NAME_WE)
add_custom_target(_asv_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "asv" "/home/ric_94/catkin_ws/src/asv/msg/rudderd.msg" ""
)

#
#  langs = gencpp;genlisp;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(asv
  "/home/ric_94/catkin_ws/src/asv/msg/compass.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/asv
)
_generate_msg_cpp(asv
  "/home/ric_94/catkin_ws/src/asv/msg/status.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/asv
)
_generate_msg_cpp(asv
  "/home/ric_94/catkin_ws/src/asv/msg/gps.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/asv
)
_generate_msg_cpp(asv
  "/home/ric_94/catkin_ws/src/asv/msg/propd.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/asv
)
_generate_msg_cpp(asv
  "/home/ric_94/catkin_ws/src/asv/msg/arduino.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/asv
)
_generate_msg_cpp(asv
  "/home/ric_94/catkin_ws/src/asv/msg/position.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/asv
)
_generate_msg_cpp(asv
  "/home/ric_94/catkin_ws/src/asv/msg/headingd.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/asv
)
_generate_msg_cpp(asv
  "/home/ric_94/catkin_ws/src/asv/msg/rudderd.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/asv
)

### Generating Services

### Generating Module File
_generate_module_cpp(asv
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/asv
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(asv_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(asv_generate_messages asv_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/ric_94/catkin_ws/src/asv/msg/compass.msg" NAME_WE)
add_dependencies(asv_generate_messages_cpp _asv_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ric_94/catkin_ws/src/asv/msg/status.msg" NAME_WE)
add_dependencies(asv_generate_messages_cpp _asv_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ric_94/catkin_ws/src/asv/msg/gps.msg" NAME_WE)
add_dependencies(asv_generate_messages_cpp _asv_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ric_94/catkin_ws/src/asv/msg/propd.msg" NAME_WE)
add_dependencies(asv_generate_messages_cpp _asv_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ric_94/catkin_ws/src/asv/msg/arduino.msg" NAME_WE)
add_dependencies(asv_generate_messages_cpp _asv_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ric_94/catkin_ws/src/asv/msg/position.msg" NAME_WE)
add_dependencies(asv_generate_messages_cpp _asv_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ric_94/catkin_ws/src/asv/msg/headingd.msg" NAME_WE)
add_dependencies(asv_generate_messages_cpp _asv_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ric_94/catkin_ws/src/asv/msg/rudderd.msg" NAME_WE)
add_dependencies(asv_generate_messages_cpp _asv_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(asv_gencpp)
add_dependencies(asv_gencpp asv_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS asv_generate_messages_cpp)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(asv
  "/home/ric_94/catkin_ws/src/asv/msg/compass.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/asv
)
_generate_msg_lisp(asv
  "/home/ric_94/catkin_ws/src/asv/msg/status.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/asv
)
_generate_msg_lisp(asv
  "/home/ric_94/catkin_ws/src/asv/msg/gps.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/asv
)
_generate_msg_lisp(asv
  "/home/ric_94/catkin_ws/src/asv/msg/propd.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/asv
)
_generate_msg_lisp(asv
  "/home/ric_94/catkin_ws/src/asv/msg/arduino.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/asv
)
_generate_msg_lisp(asv
  "/home/ric_94/catkin_ws/src/asv/msg/position.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/asv
)
_generate_msg_lisp(asv
  "/home/ric_94/catkin_ws/src/asv/msg/headingd.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/asv
)
_generate_msg_lisp(asv
  "/home/ric_94/catkin_ws/src/asv/msg/rudderd.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/asv
)

### Generating Services

### Generating Module File
_generate_module_lisp(asv
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/asv
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(asv_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(asv_generate_messages asv_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/ric_94/catkin_ws/src/asv/msg/compass.msg" NAME_WE)
add_dependencies(asv_generate_messages_lisp _asv_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ric_94/catkin_ws/src/asv/msg/status.msg" NAME_WE)
add_dependencies(asv_generate_messages_lisp _asv_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ric_94/catkin_ws/src/asv/msg/gps.msg" NAME_WE)
add_dependencies(asv_generate_messages_lisp _asv_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ric_94/catkin_ws/src/asv/msg/propd.msg" NAME_WE)
add_dependencies(asv_generate_messages_lisp _asv_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ric_94/catkin_ws/src/asv/msg/arduino.msg" NAME_WE)
add_dependencies(asv_generate_messages_lisp _asv_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ric_94/catkin_ws/src/asv/msg/position.msg" NAME_WE)
add_dependencies(asv_generate_messages_lisp _asv_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ric_94/catkin_ws/src/asv/msg/headingd.msg" NAME_WE)
add_dependencies(asv_generate_messages_lisp _asv_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ric_94/catkin_ws/src/asv/msg/rudderd.msg" NAME_WE)
add_dependencies(asv_generate_messages_lisp _asv_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(asv_genlisp)
add_dependencies(asv_genlisp asv_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS asv_generate_messages_lisp)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(asv
  "/home/ric_94/catkin_ws/src/asv/msg/compass.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/asv
)
_generate_msg_py(asv
  "/home/ric_94/catkin_ws/src/asv/msg/status.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/asv
)
_generate_msg_py(asv
  "/home/ric_94/catkin_ws/src/asv/msg/gps.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/asv
)
_generate_msg_py(asv
  "/home/ric_94/catkin_ws/src/asv/msg/propd.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/asv
)
_generate_msg_py(asv
  "/home/ric_94/catkin_ws/src/asv/msg/arduino.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/asv
)
_generate_msg_py(asv
  "/home/ric_94/catkin_ws/src/asv/msg/position.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/asv
)
_generate_msg_py(asv
  "/home/ric_94/catkin_ws/src/asv/msg/headingd.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/asv
)
_generate_msg_py(asv
  "/home/ric_94/catkin_ws/src/asv/msg/rudderd.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/asv
)

### Generating Services

### Generating Module File
_generate_module_py(asv
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/asv
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(asv_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(asv_generate_messages asv_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/ric_94/catkin_ws/src/asv/msg/compass.msg" NAME_WE)
add_dependencies(asv_generate_messages_py _asv_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ric_94/catkin_ws/src/asv/msg/status.msg" NAME_WE)
add_dependencies(asv_generate_messages_py _asv_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ric_94/catkin_ws/src/asv/msg/gps.msg" NAME_WE)
add_dependencies(asv_generate_messages_py _asv_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ric_94/catkin_ws/src/asv/msg/propd.msg" NAME_WE)
add_dependencies(asv_generate_messages_py _asv_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ric_94/catkin_ws/src/asv/msg/arduino.msg" NAME_WE)
add_dependencies(asv_generate_messages_py _asv_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ric_94/catkin_ws/src/asv/msg/position.msg" NAME_WE)
add_dependencies(asv_generate_messages_py _asv_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ric_94/catkin_ws/src/asv/msg/headingd.msg" NAME_WE)
add_dependencies(asv_generate_messages_py _asv_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ric_94/catkin_ws/src/asv/msg/rudderd.msg" NAME_WE)
add_dependencies(asv_generate_messages_py _asv_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(asv_genpy)
add_dependencies(asv_genpy asv_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS asv_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/asv)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/asv
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
add_dependencies(asv_generate_messages_cpp std_msgs_generate_messages_cpp)

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/asv)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/asv
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
add_dependencies(asv_generate_messages_lisp std_msgs_generate_messages_lisp)

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/asv)
  install(CODE "execute_process(COMMAND \"/usr/bin/python\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/asv\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/asv
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
add_dependencies(asv_generate_messages_py std_msgs_generate_messages_py)
