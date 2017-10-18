// Vector 2D
function Vector(x, y) {
    this.x = x;
    this.y = y;
}

// define methods
Vector.prototype.plus = function (other) {
    return new Vector(this.x + other.x, this.y + other.y);
};
// class grid
function Grid(rows, columns) {
    this.rows = rows;
    this.columns = columns
    this.array = Array.apply(null, new Array(this.rows * this.columns));
    this.array = this.array.map(function(i) {return '  .'});
    
    this.reset()
};
// grid methods
Grid.prototype.reset = function() {

    for (i=0; (i < this.rows * this.columns); i++) {
        if (i % this.columns == 0) {
            this.array[i] = this.array[i + this.columns - 1] = '|';
        };
    };
};

Grid.prototype.isInside = function(vector) {
    return vector.x <= this.columns && vector.y <= this.rows &&
    vector.x >= 0 && vector.y >= 0;
};

Grid.prototype.isPassable = function(pos) {
    return this.get(pos) === '  .';
}

Grid.prototype.get = function(vector) {
    return this.array[vector.y * this.columns + vector.x];
};

Grid.prototype.set = function(vector, value) {
    this.array[vector.y * this.columns + vector.x] = value;
}

Grid.prototype.show = function() {
    for (i=0; i<this.array.length; i+=this.columns) {
        console.log(this.array.slice(i, i + this.columns).join(''));
    };
};

var directions = {
    'n': {x: -1, y: 0},
    's': {x: 1, y: 0},
    'e': {x: 0, y: -1},
    'w': {x: 0, y: -1},

}

//
function Actor(pos, rot, world) {
    //no reason to do this?
    this.pos = new Vector(pos.x, pos.y);
    this.rot = rot
    this.world = world
}

Actor.prototype = {
    move: function(dir) {
        for (var i in arguments) {
            direction = arguments[i];
            
            new_pos = new Vector((this.world.rows + this.pos.x + directions[direction].x) % this.world.rows,
                                  (this.world.columns + this.pos.y + directions[direction].y) % this.world.columns);

            if (this.world.isPassable(new_pos)) {
                this.pos = new_pos;
            }
            else {
                console.log('impassable')
            }
        };
    }
}

//


// test case outside grid
var grid2d = new Grid(10, 10);
var point1 = new Vector(11, 2);
console.log('should be false: ', grid2d.isInside(point1));
console.log('should be true: ', grid2d.isInside(new Vector(10, 9)));
console.log('should be false: ', grid2d.isInside(new Vector(-1, -1)));

console.log('\n')

grid2d.set(new Vector(1, 1), 'special value')
console.log(grid2d.get(new Vector(1, 1)))

console.log(grid2d.array[0], '\n')

grid2d = new Grid(13, 13)
// grid2d.reset()
grid2d.show()
console.log('\n')

actor = new Actor({x: 0, y: 0}, {}, grid2d);
console.log(actor.pos)
actor.move('n')

for (i = 0; i < 20; i++) {
    console.log(actor.pos)
    actor.move('s')
    

    console.log(grid2d.isInside(actor.pos))
}

