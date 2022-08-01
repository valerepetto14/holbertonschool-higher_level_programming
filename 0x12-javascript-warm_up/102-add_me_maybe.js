#!/usr/bin/node
exports.addMeMaybe = function (value, func) {
  const nb = value + 1;
  func(nb);
};
