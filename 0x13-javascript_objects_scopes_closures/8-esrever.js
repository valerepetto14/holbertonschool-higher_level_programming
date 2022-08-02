exports.esrever = function (list) {
  let newlist = []
  for (let index = list.length - 1; index >= 0; index--) {
    newlist.push(list[index])
  }
	return newlist
};
