/*jshint esversion: 6 */

function Calculate_H(grade) {
	grade = parseFloat(grade);

	if (grade >= 93) {
		return 4.5;
	} else if (grade >= 90) {
		return 4.2;
	} else if (grade >= 87) {
		return 3.8;
	} else if (grade >= 83) {
		return 3.5;
	} else if (grade >= 80) {
		return 3.2;
	} else if (grade >= 77) {
		return 2.8;
	} else if (grade >= 73) {
		return 2.5;
	} else if (grade >= 70) {
		return 2.2;
	} else if (grade >= 67) {
		return 1.8;
	} else if (grade >= 63) {
		return 1.5;
	} else if (grade >= 60) {
		return 1.2;
	} else {
		return 0;
	}
}

function Calculate_S(grade) {
	grade = parseFloat(grade);

	if (grade >= 93) {
		return 4.0;
	} else if (grade >= 90) {
		return 3.7;
	} else if (grade >= 87) {
		return 3.3;
	} else if (grade >= 83) {
		return 3.0;
	} else if (grade >= 80) {
		return 2.7;
	} else if (grade >= 77) {
		return 2.3;
	} else if (grade >= 73) {
		return 2.0;
	} else if (grade >= 70) {
		return 1.7;
	} else if (grade >= 67) {
		return 1.3;
	} else if (grade >= 63) {
		return 1.0;
	} else if (grade >= 60) {
		return 0.7;
	} else {
		return 0;
	}
}

function CalculateGrade() {
	// Core Subjects Length
	let core_subs_len = document.getElementsByName("core").length;

	// Array for looping through
	let core_subs = [];

	for (let i = 0; i < core_subs_len; i++) {
		core_subs[i] = document.getElementsByName("core")[i].value;
	}

	//Elective_Subjects Array
	let elective_subs_len = document.getElementsByName("elective").length;
	let elective_subs = [];

	for (let i = 0; i < elective_subs_len; i++) {
		elective_subs[i] = document.getElementsByName("elective")[i].value;
	}

	let core_sum = 0;
	let elective_sum = 0;

	// Looping Through Core
	for (let i = 0; i < 4; i++) {
		core_sum += Calculate_H(core_subs[i]);
	}

	for (let i = 0; i < 6; i++) {
		elective_sum += Calculate_S(elective_subs[i]);
	}

	let Final_Core = core_sum * 0.5;
	let Final_Elect = elective_sum * 0.25;
	let Final = Final_Core + Final_Elect;
	let Final_Grade = Final / 3.5;

	document.getElementById("result").innerHTML =
		"<b style='font-size: 40px;'> " + Final_Grade.toFixed(2) + " </b>";
}
