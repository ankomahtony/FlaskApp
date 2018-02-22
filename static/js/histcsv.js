var width = 500,
	height = 500,
	padding = 50;

d3.csv("ages.csv", function (data){
	var map = data.map(function (i){ return parseInt(i.age);})
	

	var histogram = d3.layout.histogram()
		.bins(7)
		(map)

	var y = d3.scale.linear()
		.domain([0,d3.max(histogram.map(function (i) {return i.length;}))])
		.range([0,height]);

	var x = d3.scale.linear()
		.domain([0,d3.max(map)])
		.range([0,width])

	var xAxis = d3.svg.axis()
		.scale(x)
		.orient("bottom");

	var canvas = d3.select("body").append("svg")
		.attr({
			width: width,
			height: height + padding
		})
		.append("g")
			.attr("transform", "translate(20,0)");

	var group = canvas.append("g")
		.attr("transform", "translate(5,"+ height + ")")
		.call(xAxis);

	var bars = canvas.selectAll(".bar")
		.data(histogram)
		.enter()
		.append("g")

	bars.append("rect")
		.attr({
			x: function (d){ return x(d.x);},
			y: function (d){ return 500-y(d.y);},
			width: function (d) {return x(d.dx);},
			height: function (d) { return y(d.y);},
			fill: "steelblue"
		})

	bars.append("text")
		.attr({
			x: function (d) { return x(d.x);},
			y: function (d) { return 500 - y(d.y);},
			dy: "20px",
			dx: function (d) { return x(d.dx)/2;},
			fill: "#fff",
			"text-anchor": "middle"
		})
		.text(function (d) { return d.y; })
})