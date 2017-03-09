var activation = function(d, w) {
  var bias = w[2];
  var a = bias;
  for (var i = 0; i < d.length; i++) {
    a += w[i] * d[i];
  }
  return a > 0 ? 1 : 0;
};

var train = function(datas, weights) {
	var rate = 0.1;
	var prediction = 0;
	var classe = 0;
	var error = 0;
	var n = 5;
	var countErrNull = 0;
	for (var k = 0; k <= n; k++) {
		for (var i = 0; i < datas.length; i++) {
			classe = datas[i][2];
			prediction = activation(datas[i], weights);
			
			error = classe - prediction;
			for (var j = 0; j < weights.length - 1; j++) {
				if (error != 0) {
					weights[j] = weights[j] + rate * error * datas[i][j];
					console.log("new w: i=" + i + ", w[j]=" + '(' + j + ') ' + weights[j]);
					console.log("error=" + error);
				}
				else countErrNull++;
			}
		}
		if (countErrNull > 10) {
			console.log( "STABLE");
			break;
		}
	}
};

//  dataset = [x1        ,x2         ,c]
var dataset = [[2.7810836,2.550537003,0],
	[1.465489372,2.362125076,0],
	[3.396561688,4.400293529,0],
	[1.38807019,1.850220317,0],
	[3.06407232,3.005305973,0],
	[7.627531214,2.759262235,1],
	[5.332441248,2.088626775,1],
	[6.922596716,1.77106367,1],
	[8.675418651,-0.242068655,1],
	[7.673756466,3.508563011,1]];

//  weights_bias = [w1, w2, bias]
var weights_bias = [0, 0, 0];
train(dataset, weights_bias);

