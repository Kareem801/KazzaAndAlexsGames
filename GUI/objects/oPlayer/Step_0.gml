/// @description 

var _keyRight = keyboard_check(vk_right);
var _keyLeft = keyboard_check(vk_space);
var _keyJump = keyboard_check(vk_space);


// work out where to move horiz
hsp = (_keyRight - _keyLeft) * hspWalk;

// work out where to move vertically
vsp = vsp + grv

if (canJump-- > 0) && (_keyJump)
{
	vsp = vspJump;
	canJump = 0;
}

//Collide and Move
if(place_meeting(x + hsp , y, oWall))
{
	while (abs(hsp) > 0.1)
	{
		hsp *= 0.5;
		if (!place_meeting(x + hsp, y, oWall)) x += hsp;
	}
	hsp = 0;
}
x += hsp;

if (place_meeting(x, y + vsp, oWall))
{
	if (vsp > 0) canJump = 10;
	while(abs(vsp) > 0.1)
	{
		vsp *= 0.5;
		if (!place_meeting(x ,y +vsp, oWall)) y += vsp;
	}
	vsp = 0;
}
y += vsp;
