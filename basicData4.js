var w = window.innerWidth,
    h = window.innerHeight,
    margin = { top: 40, right: 20, bottom: 20, left: 40 },
    radius = 6;

svg = d3.select("body").append("svg").attr({
    width: w,
    height: h
});

var dataset = [
  { x: 100, y: 110 },
  { x: 83, y: 43 },
  { x: 92, y: 28 },
  { x: 49, y: 74 },
  { x: 51, y: 10 },
  { x: 25, y: 98 },
  { x: 77, y: 30 },
  { x: 20, y: 83 },
  { x: 11, y: 63 },
  { x: 4, y: 55 },
  { x: 0, y: 0 },
  { x: 85, y: 100 },
  { x: 60, y: 40 },
  { x: 70, y: 80 },
  { x: 10, y: 20 },
  { x: 40, y: 50 },
  { x: 25, y: 31 }
];

var xScale = d3.scale.linear()
  .domain([0, d3.max(dataset, function (d) {return d.x;}) + 10])
  .range([margin.left, w - margin.right]);

  var yScale = d3.scale.linear()
    .domain([0, d3.max(dataset, function (d) {return d.y;}) + 10])
    .range([margin.top, h - margin.bottom]);

var xAxis = d3.svg.axis().scale(xScale).orient("top");
var yAxis = d3.svg.axis().scale(yScale).orient("left");

var circleInitAttrs = {
  cx: xScale(0),
  cy: yScale(0),
  r: 1,
  fill: "green"
};

var circleAttrs = {
  cx: function(d){ return xScale(d.x);},
  cy: function(d){ return yScale(d.y);},
  r: radius,
  fill: "green"
};

var xAxisGroup = svg.append("g").attr({
  "class": "axis",
  transform: "translate(" + [0,margin.top] +")"
}).call(xAxis);

var yAxisGroup = svg.append("g").attr({
  "class": "axis",
  transform: "translate(" + [margin.left,0] +")"
}).call(yAxis);

function handleMouseOver (d, i) {
  d3.select(this).attr({
    fill:"orange",
    r: radius
  });
  svg.append("text")
      .attr({
          id: "t" + d.x + "-" + d.y + "-" + i,
          x: function(){ return xScale(d.x) - 30;},
          y: function(){ return yScale(d.y) - 15;}
        })
        .text(function (){
          return [d.x, d.y];
        });
}
function handleMouseOut (d, i){
    d3.select(this).attr({
      fill:"green",
      r: radius
      });
      d3.select("#t" + d.x + "-" + d.y + "-" + i).remove();
}

var circles = svg.selectAll("circle")
    .data(dataset)
    .enter()
    .append("circle")
    .attr(circleInitAttrs)
    .on("mouseover", handleMouseOver)
    .on("mouseout", handleMouseOut);

    circles.transition()
        .delay(function(d,i){
          return i*100;
        })
        .duration(1000)
        .attr(circleAttrs);

    svg.on("click", function (){
        var coords = d3.mouse(this);

        var newDataset = {
          x: Math.round(xScale.invert(coords[0])),
          y: Math.round(yScale.invert(coords[1]))
        };

        dataset.push(newDataset);

        xScale.domain([0, d3.max(dataset, function (d) { return d.x; }) + 10]);
        yScale.domain([0, d3.max(dataset, function (d) { return d.y; }) + 10]);

        xAxisGroup.transition().call(xAxis);
        yAxisGroup.transition().call(yAxis);

      var c =  svg.selectAll("circle").data(dataset)
      c.transition()
        .ease("elastic")
        .attr(circleAttrs)
      c.enter()
      .append("circle")
      .attr(circleInitAttrs)
      .on("mouseover", handleMouseOver)
      .on("mouseout", handleMouseOut);

      c.transition()
          .duration(2000)
          .attr(circleAttrs);
    });
