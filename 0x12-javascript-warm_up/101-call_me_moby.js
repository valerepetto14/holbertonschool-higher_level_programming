#!/usr/bin/node
exports.callMeMoby = function (value, funct) {
  for (let index = 0; index < value; index++) {
    funct();
  }
};
