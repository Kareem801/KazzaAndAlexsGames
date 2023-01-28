<<<<<<< HEAD
draw_sprite_stretched(sMenuBox,0,x-margin,y-margin,widthFull,heightFull)

draw_set_colour(c_white);
draw_set_font(fPixel);
draw_set_halign(fa_left);
draw_set_valign(fa_top);

var _desc = !(description == -1);
for (l = 0; l < (optionsCount + _desc); l++)
{
	draw_set_colour(c_white);
	if (l == 0) && (_desc) 
	{
		draw_text(x, y, description)
	}
	else
	{
		var _str = options[l-_desc][0]
		if (hover == l - _desc) 
		{
			draw_set_colour(c_yellow);
			_str = hovermarker+_str;	
		}
		draw_text(x, y + l * heightLine, _str);
	}
}
=======
draw_sprite_stretched(sMenuBox,0,x-margin,y-margin,widthFull,heightFull)

draw_set_colour(c_white);
draw_set_font(fPixel);
draw_set_halign(fa_left);
draw_set_valign(fa_top);

var _desc = !(description == -1);
for (l = 0; l < (optionsCount + _desc); l++)
{
	draw_set_colour(c_white);
	if (l == 0) && (_desc) 
	{
		draw_text(x, y, description)
	}
	else
	{
		var _str = options[l-_desc][0]
		if (hover == l - _desc) 
		{
			draw_set_colour(c_yellow);
			_str = hovermarker+_str;	
		}
		draw_text(x, y + l * heightLine, _str);
	}
}
>>>>>>> 7ae79da1a225ed08995f163bce5510334e013f32
