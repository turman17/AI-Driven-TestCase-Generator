<script setup lang="ts">
import UserStoryForm from '@/components/Input/UserStoryForm.vue'
import TestCasesOutput from '@/components/Output/TestCasesOutput.vue'
import type TestCase from './types/TestCase'
import { ref } from 'vue'

const outputFile = ref('')
const testCasesTitle = ref('')
const testCasesArray = ref<Array<TestCase>>([])

const clearFiles = () => {
	outputFile.value = ''
	testCasesTitle.value = ''
	testCasesArray.value = []
}

const handleCreateCase = (testCase: TestCase) => {
	testCasesArray.value.push(testCase)
}

const handleDeleteCase = (index: number) => {
	testCasesArray.value.splice(index, 1)
}

const handleUpdateTestCases = (title: string, testCases: Array<TestCase>) => {
	testCasesTitle.value = title
	testCasesArray.value = testCases
}

const handleGenerateFile = (filename: string) => {
	outputFile.value = filename
}
</script>

<template>
	<header>
		<div class="nav-content">
			<img src="./assets/logo-axians.png" alt="Axians Logo" class="logo" />
			<h1>Open Your Mind Hackathon</h1>
		</div>
		<div class="border-bottom"></div>
	</header>

	<main>
		<user-story-form
			@processing-file="clearFiles"
			@update-test-cases="handleUpdateTestCases"
			@clear-results="clearFiles"
			:test-cases="testCasesArray"
		/>
		<test-cases-output
			v-if="testCasesTitle.length > 0"
			:file-name="outputFile"
			:title="testCasesTitle"
			:test-cases="testCasesArray"
			@create-case="handleCreateCase"
			@delete-case="handleDeleteCase"
			@generate-file="handleGenerateFile"
		/>
	</main>
</template>

<style>
* {
	box-sizing: border-box;
	padding: 0;
	margin: 0;
	--crimson: #a20067;
	--blue: #005eb8;
	font-family: Arial, Helvetica, sans-serif;
}
header {
	/* padding: 1rem; */
	position: sticky;
	top: 0;
	background: white;
	z-index: 100;
}

.nav-content {
	display: flex;
	align-items: center;
	gap: 1.5rem;
	margin-left: 2rem;
	margin-block: 1.2rem;
	padding-bottom: 0.5rem;
}

.border-bottom {
	height: 2px;
	width: 100%;
	z-index: 100;
	background-color: #f8f9fa;
	box-shadow: 0 4px 6px -3px black;
}

.logo {
	width: 100px;
}

main {
	margin-top: 40px;
}
</style>
