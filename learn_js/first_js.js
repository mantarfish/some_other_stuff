function createDisplay() {
    var display = document.createElement("div");
    display.className = "display";
    document.body.appendChild(display)
}

function createActor() {
    var display = document.body.querySelector("div");
    var actor = document.createElement("Actor");
    actor.className = "actor"
    display.appendChild(actor);
}

function Actor() {
    this.pos = [0, 0];
}

Actor.prototype.move = function (direction) {
    this.pos = [this.pos[0] + direction[0], this.pos[1] + direction[1]]
}
mov = [1, 1];

function update() {
    var actor = document.body.querySelector("Actor");
    window.requestAnimationFrame(update);

    now = Date.now();
    if (now - then > 1) {


        if (actor1.pos[0] > 97)
            mov[0] = -1;
        if (actor1.pos[1] > 152)
            mov[1] = -1;
        if (actor1.pos[0] < 2)
            mov[0] = 1;
        if (actor1.pos[1] < 2)
            mov[1] = 1;

        actor1.move(mov)
        actor.style.left = actor1.pos[0] + "px";
        actor.style.top = actor1.pos[1] + "px";

        then = now;
    }


}


actor1 = new Actor()


createDisplay();
createActor();

var then = Date.now();

update();
