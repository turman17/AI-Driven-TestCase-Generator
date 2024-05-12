<template>
	<div class="modal-container" @click="closeModal">
		<div class="modal-content" @click.stop>
			<form @click.stop @submit.prevent="handleEditTest">
				<label for="title">Title</label>
				<input type="text" name="title" v-model="localTestCase.title" />
				<label for="testId">Test Case Id</label>
				<input type="text" name="testId" v-model="localTestCase.testCaseId" />
				<label for="description" class="label description">Description</label>
				<textarea
					class="textarea description"
					type="text"
					name="description"
					v-model="localTestCase.description"
				/>
				<label class="label-with-button">
					Pre-conditions
					<button class="add-condition-btn" @click.prevent="addNewPrecondition">
						Add Pre-condition
					</button>
				</label>
				<div v-for="(preCondition, index) in localTestCase.preConditions" :key="index">
					<textarea
						v-model="localTestCase.preConditions[index]"
						class="textarea pre-condition"
					></textarea>
					<button class="delete-btn" @click.prevent="deletePrecondition(index)">
						Delete
					</button>
				</div>
				<label class="label-with-button">
					Actions
					<button class="add-action-btn" @click.prevent="addNewAction">Add Action</button>
				</label>
				<div v-for="(action, index) in localTestCase.actions" :key="'action-' + index">
					<label>Steps</label>
					<textarea v-model="action.step" class="textarea action-step"></textarea>
					<label for="expectedResults">Expected Results</label>
					<div class="expected-results">
						<input
							type="text"
							v-for="(result, resultIndex) in action.expectedResults"
							:key="'result-' + resultIndex"
							v-model="action.expectedResults[resultIndex]"
							class="expected-result"
						/>
						<button
							class="add-expected-result-btn"
							@click.prevent="addExpectedResult(index)"
						>
							Add Expected Result
						</button>
					</div>
					<button class="delete-btn" @click.prevent="deleteAction(index)">
						Delete Action
					</button>
				</div>
				<button class="create-test-btn" type="submit">Create test case</button>
			</form>
		</div>
	</div>
</template>

<script setup lang="ts">
import type TestCase from '@/types/TestCase'
import { ref } from 'vue'

const emit = defineEmits(['close', 'create-case'])

const localTestCase = ref<TestCase>({
	title: '',
	testCaseId: '',
	description: '',
	requirement: [''],
	preConditions: [],
	actions: []
})

const closeModal = () => {
	emit('close')
}

const addNewPrecondition = () => {
	localTestCase.value.preConditions.push('')
}

const deletePrecondition = (index: number) => {
	localTestCase.value.preConditions.splice(index, 1)
}

const addNewAction = () => {
	localTestCase.value.actions.push({
		step: '',
		expectedResults: ['']
	})
}

const addExpectedResult = (actionIndex: number) => {
	localTestCase.value.actions[actionIndex].expectedResults.push('')
}

const deleteAction = (index: number) => {
	localTestCase.value.actions.splice(index, 1)
}

const handleEditTest = () => {
	console.log(localTestCase.value)
	emit('create-case', localTestCase.value)
	emit('close')
}
</script>

<style scoped>
.modal-container {
	position: fixed;
	top: 0;
	left: 0;
	width: 100%;
	height: 100%;
	background-color: rgba(0, 0, 0, 0.8); /* semi-transparent background */
	display: flex;
	justify-content: center;
	align-items: center;
	z-index: 150;
}

.modal-content {
	position: relative;
	height: 90vh;
	overflow: scroll;
	background-color: white;
	padding: 20px;
	border-radius: 8px;
	box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.3); /* shadow effect */
}

form {
	width: 800px; /* adjust width as needed */
	display: flex;
	flex-direction: column;
	justify-content: center;
}

.label {
	display: block;
	margin-bottom: 5px;
}

textarea,
input[type='text'] {
	width: 100%;
	padding: 8px;
	margin-bottom: 10px; /* Add margin between fields */
	box-sizing: border-box;
}

textarea.pre-condition,
.requirement {
	margin-bottom: 0; /* Remove margin between pre-condition textareas */
}

.label-with-button {
	display: flex;
	justify-content: space-between;
	align-items: center;
	margin-bottom: 5px;
}

.add-condition-btn,
.add-action-btn {
	background-color: var(--crimson);
	color: white;
	border: none;
	padding: 5px 10px;
	cursor: pointer;
	width: 150px; /* Adjust as needed */
}

.delete-btn,
.add-expected-result-btn {
	background-color: var(--crimson);
	color: white;
	border: none;
	padding: 5px 10px;
	cursor: pointer;
	margin-bottom: 1rem;
}

.create-test-btn {
	background-color: var(--crimson);
	color: white;
	border: none;
	padding: 10px 20px;
	cursor: pointer;
	width: 90%;
	margin: 1rem auto;
}

button:hover {
	background-color: #8a0057;
}
</style>
