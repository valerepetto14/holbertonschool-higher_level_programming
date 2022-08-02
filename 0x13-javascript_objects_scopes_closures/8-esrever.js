exports.esrever = function (list) {
  return list.reduce((acc, val) =>  [val, ...acc], [])
};
