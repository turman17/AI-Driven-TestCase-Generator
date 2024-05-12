<template>
	<div class="download-wrapper">
		<button class="generate-file-button" @click="handleGenerateFile">Generate file</button>
		<a
			v-if="fileName.length"
			:href="`http://localhost:8000/static/${fileName}.docx`"
			class="download-link"
			>Download .docx</a
		>
		<a
			v-if="fileName.length"
			:href="`http://localhost:8000/static/${fileName}.csv`"
			class="download-link"
			>Download .csv</a
		>
	</div>
</template>

<script lang="ts" setup>
import type TestCase from '@/types/TestCase'
const props = defineProps({
	fileName: {
		type: String,
		required: true
	},
	testCases: {
		type: Array<TestCase>,
		required: true
	},
	title: {
		type: String,
		required: true
	}
})

const emit = defineEmits(['generateFile'])

const handleGenerateFile = async () => {
	const docContents = {
		title: props.title,
		testCases: props.testCases
	}
	const asString = JSON.stringify(docContents)
	try {
		const response = await fetch('http://localhost:8000/generate', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: asString
		})
		const data = await response.json()
		console.log(data)
		const { file_path } = data
		emit('generateFile', file_path)
	} catch (error) {
		console.error(error)
	}
}
</script>

<style scoped>
.download-wrapper {
	display: flex;
	justify-content: space-around;
	margin: 0 auto 2rem;
	width: 60%;
}

.download-link {
	text-decoration: none;
	color: white;
	background-color: var(--crimson);
	border-radius: 5px;
	padding: 0.5rem 1rem;
}

.download-link:hover {
	border: 2px solid var(--crimson);
	color: black;
	background-color: white;
}

.generate-file-button {
	text-decoration: none;
	color: white;
	background-color: var(--crimson);
	border-radius: 5px;
	padding: 0.5rem 1rem;
	border: none;
}

.generate-file-button:hover {
	border: 2px solid var(--crimson);
	color: black;
	background-color: white;
	cursor: pointer;
}
</style>
