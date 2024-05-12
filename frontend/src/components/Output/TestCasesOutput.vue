<template>
	<h1>{{ `${testCases.length} ${title}` }}</h1>
	<download-wrapper
		:file-name="fileName"
		:test-cases="testCases"
		:title="title"
		@generate-file="handleGenerateFile"
	/>
	<div class="instructions" v-if="testCases && testCases.length">
		<h2>Usage</h2>
		<ul>
			<li>Open each test case and check its validity</li>
			<li>If needed, click the "Edit test case" button and edit the fields</li>
			<li>You can also delete the test cases and/or add new ones</li>
			<li>When everything is done, click on "Generate file" to create .docx and .csv file</li>
		</ul>
	</div>
	<output-text-wrapper
		:test-cases="testCases"
		@create-case="handleCreateCase"
		@delete-case="handleDeleteCase"
	/>
</template>

<script lang="ts" setup>
import DownloadWrapper from '@/components/Output/DownloadWrapper.vue'
import OutputTextWrapper from './OutputTextWrapper.vue'
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

const emit = defineEmits(['create-case', 'delete-case', 'generate-file'])

const handleCreateCase = (testCase: TestCase) => {
	emit('create-case', testCase)
}

const handleDeleteCase = (index: number) => {
	emit('delete-case', index)
}

const handleGenerateFile = (filename: String) => {
	emit('generate-file', filename)
}
</script>

<style scoped>
h1 {
	text-align: center;
	margin-bottom: 1rem;
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
	margin: 0 auto;
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
