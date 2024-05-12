<template>
	<edit-test-modal
		v-if="isEditing && chosenTestCase"
		@close="isEditing = false"
		:test-case="chosenTestCase"
	/>
	<create-test-case
		v-if="isCreating"
		@close="isCreating = false"
		@create-case="handleCreateCase"
	/>
	<div class="text-wrapper">
		<button class="add-test-case" @click="isCreating = true">Add test case</button>
		<div v-for="(testCase, index) in testCases" :key="index" class="test-case">
			<button
				@click="toggleCollapse(index)"
				:class="{ active: !isCollapsed(index) }"
				class="collapsible"
			>
				{{ testCase.title }}
			</button>
			<div v-if="!isCollapsed(index)" class="content">
				<div class="action-buttons">
					<button class="editTest" @click="handleEditCase(testCase)">
						Edit test case
					</button>
					<button class="delete-test-case" @click="deleteTestCase(index)">
						Delete test case
					</button>
				</div>
				<p><strong>Test Case:</strong> {{ testCase.testCaseId }}</p>
				<p><strong>Description:</strong> {{ testCase.description }}</p>
				<p><strong>Pre-Conditions:</strong></p>
				<ul>
					<li v-for="(preCondition, idx) in testCase.preConditions" :key="idx">
						{{ preCondition }}
					</li>
				</ul>
				<p><strong>Requirement:</strong> {{ testCase.requirement.join(', ') }}</p>
				<table class="actions-results">
					<thead>
						<tr>
							<th>Actions</th>
							<th>Expected Results</th>
						</tr>
					</thead>
					<tbody>
						<tr v-for="(action, idx) in testCase.actions" :key="idx">
							<td>{{ action.step }}</td>
							<td>
								<ul>
									<li
										v-for="(result, resultIdx) in action.expectedResults"
										:key="resultIdx"
									>
										{{ result }}
									</li>
								</ul>
							</td>
						</tr>
					</tbody>
				</table>
			</div>
		</div>
	</div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import type TestCase from '@/types/TestCase'
import EditTestModal from '@/components/Output/EditTestModal.vue'
import CreateTestCase from '@/components/Output/CreateTestCase.vue'

const chosenTestCase = ref<TestCase | null>(null)

defineProps({
	testCases: {
		type: Array<TestCase>,
		required: true
	}
})

const emit = defineEmits(['create-case', 'delete-case'])

const activeIndex = ref<number | null>(null)
const isEditing = ref(false)
const isCreating = ref(false)

const toggleCollapse = (index: number) => {
	if (activeIndex.value === index) {
		activeIndex.value = null
	} else {
		activeIndex.value = index
	}
}

const isCollapsed = (index: number) => {
	return activeIndex.value !== index
}

const handleEditCase = (testCase: TestCase) => {
	console.log('Editing test case:', testCase)
	isEditing.value = true
	chosenTestCase.value = testCase
}

const handleCreateCase = (testCase: TestCase) => {
	emit('create-case', testCase)
	console.log('Creating test case:', testCase)
}

const deleteTestCase = (index: number) => {
	// console.log('Deleting test case:', testCases[index])
	emit('delete-case', index)
}
</script>

<style scoped>
.text-wrapper {
	max-width: 1000px;
	margin: 0 auto;
	margin-bottom: 150px; /* Fixed bottom margin for entire accordion */
}

.test-case {
	margin-bottom: 10px; /* Add some space between test cases */
}

.collapsible {
	background-color: white;
	color: black;
	cursor: pointer;
	padding: 18px;
	width: 100%;
	border: none;
	border-bottom: 1px solid #ddd;
	text-align: left;
	outline: none;
}

.collapsible:hover {
	background-color: #f1f1f1;
}

.collapsible.active {
	background-color: var(--crimson);
	color: white;
	border-bottom: none;
	padding: 18px; /* Reset padding for active state */
}

.collapsible.active + .content {
	background-color: rgba(162, 0, 103, 0.1); /* Very slight background color */
	transition: max-height 0.5s ease-out; /* Adjusted transition duration */
	max-height: 1000px; /* Adjusted height for open collapsible */
	padding: 20px 25px 25px; /* Adjust padding for content in active state */
}

.content li {
	margin-left: 20px;
}

.collapsible::before {
	content: '\002B'; /* Plus sign '+' */
	color: #777; /* Default color for plus sign */
	font-size: 1.2em;
	float: right;
	margin-left: 5px;
	transition: transform 0.5s; /* Adjust transition duration */
}

.collapsible.active::before {
	content: '\2212'; /* Minus sign '-' */
	color: white;
}

.content {
	padding: 0 18px;
	overflow: scroll;
	transition: max-height 0.5s ease-out; /* Smooth sliding animation */
	max-height: 0; /* Initially hide content */
	display: flex;
	flex-direction: column;
	gap: 0.5rem;
}

.actions-results {
	width: 100%;
	border-collapse: collapse;
}

.actions-results th,
.actions-results td {
	border: 1px solid #ddd;
	padding: 8px;
}

.actions-results th {
	background-color: rgba(100, 3, 9, 0.1);
	text-align: left;
}

.editTest,
.delete-test-case {
	background-color: var(--crimson);
	color: white;
	border: none;
	padding: 10px;
	margin-bottom: 5px;
	cursor: pointer;
	width: 20%;
	margin: 0 auto 1rem;
}

.editTest:hover,
.delete-test-case:hover {
	background-color: #8a0057;
}

.add-test-case {
	background-color: var(--crimson);
	color: white;
	border: none;
	padding: 10px 20px;
	margin-top: 20px;
	cursor: pointer;
	border-radius: 5px;
	margin: 1rem auto;
}

.add-test-case:hover {
	background-color: #8a0057;
}

.action-buttons {
	width: 70%;
	margin: 0 auto;
	display: flex;
	justify-content: space-around;
	gap: 1rem;
}
</style>
