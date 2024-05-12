<template>
	<button v-if="testCases.length" class="clear-results-btn" @click.prevent="handleClearResults">
		Clear results
	</button>
	<div v-else class="instructions">
		<h2>Usage</h2>
		<ul>
			<li>
				Click the "Choose file" / "Browse" button and chose a valid User Story to upload.
			</li>
			<li>Optional: input extra instructions for the AI model.</li>
			<li>Click on "Get test cases" to generate the test cases.</li>
		</ul>
	</div>
	<div v-if="isLoading" class="loading-spinner">
		<loading-spinner v-if="isLoading" />
		<h2 class="loadingText">Processing...</h2>
	</div>
	<form class="user_story_form" @submit.prevent="handleFileSubmit">
		<textarea
			class="extra-instructions"
			name="extra-instructions"
			id=""
			cols="30"
			rows="5"
			placeholder="Input extra instructions for the AI model."
			v-model="extraInstructions"
		></textarea>
		<input
			type="file"
			name="file"
			accept=".docx"
			@change="selectFile"
			:key="fileInputRerender"
			required
		/>
		<button type="submit">Get test cases</button>
	</form>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import LoadingSpinner from '@/components/Loading/LoadingSpinner.vue'
import type TestCase from '@/types/TestCase'

defineProps({
	testCases: {
		type: Array<TestCase>,
		default: []
	}
})

const files = ref<HTMLInputElement>()
const isLoading = ref(false)
const fileInputRerender = ref(0)
const extraInstructions = ref('')

const emit = defineEmits(['processingFile', 'updateTestCases', 'clearResults'])

const selectFile = (e: Event) => {
	const inputElement = e.target as HTMLInputElement
	// @ts-ignore
	files.value = inputElement?.files[0] || null
}

const handleFileSubmit = async (e: Event) => {
	if (!files.value) {
		return
	}
	emit('processingFile')
	const formData = new FormData()
	formData.append('file', files.value as unknown as File)
	formData.append('extraInstructions', extraInstructions.value as string)
	try {
		isLoading.value = true
		const response = await fetch('http://localhost:8000/', {
			method: 'POST',
			body: formData
		})
		if (!response.ok) {
			const err = await response.json()
			console.log(err)
			throw new Error(err.message)
		}
		const data = await response.text()
		const jsonMatch = data.match(/\{[\s\S]*\}/)

		if (jsonMatch) {
			// Extract the JSON object
			const jsonString = jsonMatch[0]

			// Parse the JSON string into a JavaScript object
			const jsonData = JSON.parse(jsonString)

			// Print the object
			console.log(jsonData)
			emit('updateTestCases', jsonData.title, jsonData.testCases)
			isLoading.value = false
		} else {
			console.log('No JSON object found in the provided string.')
			isLoading.value = false
		}
	} catch (error) {
		console.error(error)
		isLoading.value = false
	}
}

const handleClearResults = () => {
	emit('clearResults')
}
</script>

<style scoped>
.user_story_form {
	display: flex;
	flex-direction: column;
	align-items: center;
	width: 80%;
	height: 250px;
	margin: 0 auto;
}

.loadingText {
	color: white;
	z-index: 100;
	text-align: center;
	position: fixed;
	top: 70%;
	width: 100%;
}

.loading-spinner {
	background-color: rgba(0, 0, 0, 0.8);
	position: absolute;
	width: 100vw;
	height: 100vh;
	top: 0;
	left: 0;
	z-index: 200;
}

.user_story_form button,
.clear-results-btn {
	padding: 12px 24px;
	margin: 16px 0;
	background-color: var(--crimson);
	color: white;
	border: none;
	border-radius: 4px;
	cursor: pointer;
	transition: background-color 0.3s ease; /* Add smooth transition */
	width: 200px; /* Set button width */
}

.user_story_form button:hover {
	background-color: #8a0057; /* Darken the button color on hover */
}

.extra-instructions {
	width: calc(100% - 32px); /* Adjust width to fit container */
	max-width: 100%;
	padding: 12px;
	margin-bottom: 16px; /* Increase margin */
	border: 1px solid #ccc;
	border-radius: 4px;
	box-sizing: border-box;
	resize: vertical;
}

.clear-results-btn {
	margin: -2rem auto 1rem;
	display: block;
}

.instructions h2 {
	margin-bottom: 0.5rem;
}

.instructions {
	background-color: #ffffe0; /* Very light yellow color */
	border: 2px solid #e0e0e0; /* Light border color */
	border-radius: 10px; /* Rounded corners */
	padding: 20px; /* Padding inside the box */
	font-family: Arial, sans-serif; /* Modern font */
	box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1); /* Soft shadow */
	width: 60%;
	margin: 1rem auto;
}

.instructions ul {
	list-style-type: none; /* Remove default list styles */
	padding: 0;
}

.instructions ul li {
	margin-bottom: 10px; /* Spacing between list items */
}

.instructions ul li::before {
	content: '\2022'; /* Bullet character */
	color: #808080; /* Bullet color */
	font-size: 12px; /* Bullet size */
	display: inline-block;
	width: 1em;
	margin-left: -1em; /* Position bullet properly */
}
</style>
