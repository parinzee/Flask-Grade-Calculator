/*jshint esversion: 6*/
function CalculateGrade() {
	let grade = [];

	for (let i = 0; i < 5; i++) {
		grade[i] = document.getElementsByName("sub")[i].value;
	}

	let Final = 0;

	for (let i = 0; i < 5; i++) {
		Final += parseFloat(grade[i]);
	}

	Final = Final / 5;

	if (isNaN(Final)) {
		document.getElementById("result").innerHTML =
			"<b style='font-size: 20px;'> " + "Calculating..." + " </b>";
	} else {
		document.getElementById("result").innerHTML =
			"<b style='font-size: 40px;'> " + Final + " </b>";
	}
}
