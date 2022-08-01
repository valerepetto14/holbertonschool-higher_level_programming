#!/usr/bin/node
exports.addMeMaybe = function (value, func) {
    nb = value + 1;
    func(nb)
}