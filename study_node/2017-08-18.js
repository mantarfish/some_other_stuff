/* var str = '#';
for (i = 0; i<10; i++) {
    
    console.log(str);
    str += '#';
}

///fizfuzz

for (i = 0; i<10; i++) {
    var fizz = 0;
    var fuzz = 0;

    if (i % 3 === 0)
        fizz = 1;

    if (i % 5 === 0)
        fuzz = 1;

    if (fizz == 1 && fuzz !== 1)
        console.log('fizz');
    if (fizz !== 1 && fuzz == 1)
        console.log('fuzz');
    if (fizz === fuzz === 1)
        console.log('fizzfuzz');
    if (fizz == fuzz == 0)
        console.log(i);
}
 */
/* 
size = 8;
str = '';

for (x=0; x<size; x++) {
    str += '# ';
}

for (i=0; i<10; i++) {
    
    if (i % 2 == 0)
        console.log(' ' + str);
    else
        console.log(str + ' ');
} */
/* 
var deepEqual = function (obj1, obj2) {

    for (i=0; i<2; i++) {
        if (obj1[i] !== obj2[i])
            return false;
    }

    return true;

}

var fizzfuzzer = function (code, i) {
    var rule_dict = {};
    rule_dict[String([1, 0])] = 'fizz';
    rule_dict[String([0, 1])] = 'fuzz';
    rule_dict[String([1, 1])] = 'fizzfuzz';
    rule_dict[String([0, 0])] = i;

    return rule_dict[code]
}

for (i=0; i<10; i++) {
    var code = [0, 0];
    if (i % 3 === 0)
        code[0] = 1;
    if (i % 5 === 0)
        code[1] = 1;
    // console.log(code);
    console.log(fizzfuzzer(code, i));

}

console.log([0,0] === [0,0]) */

// console.log(String([1,1,1]))

// l = {}
// l[String([1, 1])] = 1
// console.log(l)

// // Your code here.
// var firstIsChar = function (str, char) {
//     if (str.charAt(0) === char)
//       return true; 
//     else
//       return false;
//   };
  
//   var countChar = function (str, char, counter) {
//     if (counter == undefined)
//       counter = 0;
//     if (str.length == 0)
//       return counter;
  
//     if (firstIsChar(str, char) == true)
//       counter += 1;
//     str = str.substr(1);
  
//     return countChar(str, char, counter);
  
//   };
  
//   var countBs = function (str) {
//       return countChar(str, 'B');
  
//   }
  
  
//   console.log(countBs("BBC"));
//   // → 2
//   console.log(countChar("kakkerlak", "k"));
//   // → 4


// //////////////////// range function ///////////////
// function negative (iterable) {
// 	for (var i in iterable) {
//      	iterable[i] *= -1;
//     };
//   	return iterable;
// }



// function negative_range (start, end) {
  
// 	if (start < 0 && end > 0) {
//       	ret = negative(range(Math.abs(start), 0)).concat(range(0, end));
//     }
  
//   	if (start < 0 && end < 0) {
//     	ret = negative(range(Math.abs(start), Math.abs(end))); 
//     }
  
//   	return ret;
// }


// function range (start, end, step) {
//   	if (step == undefined) step = 1;
  
//   	if (start > end) {
//         var t = end;
//         end = start;
//       	end += 1;
//         start = t;
//       	start += 1;
      
//       	step = -1 * step;
//     }
      
  
// 	ret = [];
//     for (i=0; i < end; i++) {
//     	ret.push(i);
//     }
  
//   	ret = ret.slice(start);
  	
//   	if (step < 0) 
//       	ret.reverse();
//   		step = Math.abs(step)
        
// 	if (start < 0) {
//     	ret = negative_range(start, end)
//     }
        

        
//   	stepedRet = [];
//   	for (var i in ret) {
      	
//       	if (i % step == 0)
//           	stepedRet.push(ret[i]);
//     }
  	
//     return stepedRet;
// }

// function sum (iterable) {
//   	if (iterable.length == 0) return 0;
// 	return iterable.reduce(function (x, y) {return x + y;})
// }

// console.log(range(1, 10));
// // → [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
// console.log(range(5, 0, -2));
// // → [5, 4, 3, 2]
// console.log(sum(range(1, 10)));
// // → 55
// console.log(range(3, 10, 2));

// console.log(range(-4, 10));

// console.log(range(6, 3));

// ////////////////// nested list obj //////////////////////

// function arrayToList(iterable) {
//     list = {};
//     function constructList (iterable, rest, counter) {
      
//       if (counter == undefined) counter = 0;
//       if (counter == iterable.length) return 0;
      
//       rest.value = iterable[counter];
//       rest.rest = {};
//       if (counter + 1 == iterable.length) rest.rest = null;
//       counter += 1;
//         return constructList(iterable, rest.rest, counter)};
      
//     if (constructList(iterable, list) === 0)
//         return list;
//   }
  
//   function listToArray (nestedList, nth) {
//     raveledArray = [];
//     function constructArray (nested) {
//       raveledArray.push(nested.value);
//       if (nested.rest == null || raveledArray.length - 1 == nth)
//         return 0;
//       else
//         return constructArray(nested.rest);
  
//     }
//     constructArray(nestedList)  
//     return raveledArray
//   }
  
//   function nth (nested, nth) {return listToArray(nested, nth).pop()};
  
//   function prepend (element, nested) {
//     return {value: element,
//             rest: nested};
//   }
  
//   console.log(arrayToList([10, 20]));
//   // → {value: 10, rest: {value: 20, rest: null}}
//   console.log(arrayToList([1, 2, 3, 65, 8]));
  
//   console.log(listToArray(arrayToList([10, 20, 30])));
//   // → [10, 20, 30]
//   console.log(prepend(10, prepend(20, null)));
//   // → {value: 10, rest: {value: 20, rest: null}}
//   console.log(nth(arrayToList([10, 20, 30, 40]), 0));
//   // → 20

//   ////////////////////// could not get neighbor //////////////////
//   // Your code here.
// function getNeighbors () {};

// function linearize (nested) {
//   current = []
//   current.push(nested[0]);
//   visited = []
//   while (current) {
//     visiting = current.shift();
//  	neighbors = getNeighbors(visiting);
//     for (neighbor in neighbors) {
//     	if (neighbors[neighbor] !in visited) current.concat(neighbors[neighbor]);
//     visited.push(visiting);
//     }
//   }
//   return visited
// }

// var obj = {here: {is: "an"}, object: 2};
// console.log(deepEqual(obj, obj));
// // → true
// console.log(deepEqual(obj, {here: 1, object: 2}));
// // → false
// console.log(deepEqual(obj, {here: {is: "an"}, object: 2}));
// // → true
// var a = 2
// var o = {'is': 'an'}
// var s = 'string'
// console.log(a === Object(a))
// console.log(o === Object(o))
// // console.log(s === Object(s))

// var loop = [1, 2, 3]
// while (true) {
//     var head = loop.shift();
//     loop.push(head);
//     console.log(loop);
// }

function search (iterable) {
    var item = []
    var next = Object.values(iterable);
    while (true) {
      console.log('next is', next)
      current = next.shift();
      console.log('current is', current);
      if (current === Object(current)) {
        next.push(Object.values(current));
        console.log('to_next', Object.values(current), next);
      }
      else {
        item.push(current);
        console.log('to_item');
      }
      console.log('length is', next.length)
    return item;
    }
  }
    
  
  
  console.log(search(obj))
  var obj = {here: {is: "an"}, object: 2};

/// flatten array ///
  var arrays = [[1, 2, 3], [4, 5], [6]];
  
  function _flatten (array) {
    queue = array;
    flattened = []
    while (queue.length > 0) {
      cur = queue.shift();
   
        if (cur.length > 1) {
        queue = queue.concat(cur);
      }
      else {
        flattened = flattened.concat(cur);
      }
    }
    return flattened.sort();
  }
  
  function flatten (arrays) {
    return arrays.reduce ( function (i, j) {
      return i.concat(j);
    });
  }
  
  console.log(flatten(arrays))

  //////////////////////// average /////////////////////////////////
  function average(array) {
    function plus(a, b) { return a + b; }
    return array.reduce(plus) / array.length;
  }
  
  var byName = {};
  ancestry.forEach(function(person) {
    byName[person.name] = person;
  })
  
  // Your code here.
  var data = JSON.parse(ANCESTRY_FILE);
  //console.log(typeof ANCESTRY_FILE);
  
  function forEach(iterable, func) {
      for (var i in iterable) {
          func(iterable[i]);
      }
  }
  
  console.log(data)
  //////
  ageDiff = [];
  forEach(byName, function (i) {
    if (i.mother in byName) {
      motherBorn = byName[i.mother].born;
        ageDiff.push(i.born - motherBorn);
    }
  });
  
  console.log(average(ageDiff))
  
  // → 31.2

  /////////////////////// groupbycenture average age /////////////
  function average(array) {
    function plus(a, b) { return a + b; }
    return array.reduce(plus) / array.length;
  }
  
  function century(people) {
    return Math.ceil(people.died / 100);
  }
  
  function forEach(iterable, func) {
    for (var i in iterable) {
      func(iterable[i])
    }
  }
  
  var byName = {};
  ancestry.forEach(function(person) {
    byName[person.name] = person;
  })
  
  forEach(byName, function(i){
    i.century = century(i)
  })
  
  byCentury = {}
  forEach(byName, function(i){
    if (byCentury[i.century] == undefined) byCentury[i.century] = [];
    byCentury[i.century].push(i.died - i.born)
  })
  
  forEach(byCentury, function(i){
    console.log(average(i))
  })
  
  //console.log(byCentury)
  
  // Your code here.
  
  // → 16: 43.5
  //   17: 51.2
  //   18: 52.8
  //   19: 54.8
  //   20: 84.7
  //   21: 94