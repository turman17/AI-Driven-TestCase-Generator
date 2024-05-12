<template>
	<div class="loader">
		<span class="up left"></span>
		<span class="up right"></span>
		<span class="down left"></span>
		<span class="down right"></span>
	</div>
</template>

<style scoped>
* {
	margin: 0;
	padding: 0;
	box-sizing: border-box;
}

.loader {
	position: absolute;
	top: 50%;
	left: 50%;
	transform: translate(-50%, -50%);
}

span {
	position: absolute;
	width: 80px;
	height: 80px;
	background: #262626;
	animation: animate 4s infinite ease-in-out;
}

.up.left {
	background-color: var(--blue);
	left: -95px;
	top: -95px;
	animation-delay: 0ms;
}

.up.right {
	background-color: var(--crimson);
	top: -95px;
	animation-delay: 200ms;
}

.down.left {
	background-color: var(--crimson);
	left: -95px;
	animation-delay: 600ms;
}

.down.right {
	background-color: var(--blue);
	animation-delay: 400ms;
}

@keyframes animate {
	0% {
		transform: rotateY(0deg);
	}

	20% {
		transform: rotateY(360deg);
	}

	40% {
		transform: rotateX(180deg);
	}

	60% {
		transform: rotateX(0deg);
	}

	80% {
		transform: rotateX(-180deg);
	}

	100% {
		transform: rotateY(0deg);
	}
}
</style>
