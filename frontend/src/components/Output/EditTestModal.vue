<template>
	<div class="modal-container" @click="closeModal">
		<div class="modal-content" @click.stop>
			<h2 class="test-title">{{ localTestCase.title }}</h2>
			<form @click.stop @submit.prevent="handleEditTest">
				<label for="testId">Test Case</label>
				<input type="text" name="testId" v-model="localTestCase.testCaseId" />
				<label for="description" class="label description">Description</label>
				<textarea
					class="textarea description"
					type="text"
					name="description"
					v-model="localTestCase.description"
				/>
				<label>Requirement</label>
				<input
					type="text"
					class="requirement"
					v-for="(requirement, index) in localTestCase.requirement"
					:key="index"
					v-model="localTestCase.requirement[index]"
				/>
				<label>Pre-conditions</label>
				<textarea
					v-for="(preCondition, index) in localTestCase.preConditions"
					:key="index"
					v-model="localTestCase.preConditions[index]"
					class="textarea pre-condition"
				/>
				<label>Actions</label>
				<div class="actions-container">
					<div
						v-for="(action, index) in localTestCase.actions"
						:key="index"
						class="action"
					>
						<label for="actionStep">Action Step {{ index + 1 }}</label>
						<textarea
							v-model="localTestCase.actions[index].step"
							class="textarea action-step"
						></textarea>
						<label for="expectedResults">Expected Results</label>
						<div class="expected-results">
							<input
								type="text"
								v-for="(result, resultIndex) in action.expectedResults"
								:key="resultIndex"
								v-model="localTestCase.actions[index].expectedResults[resultIndex]"
								class="expected-result"
							/>
						</div>
					</div>
				</div>
				<button>Update</button>
			</form>
		</div>
	</div>
</template>

<script lang="ts" setup>
import { ref } from 'vue'
const emit = defineEmits(['close'])
const props = defineProps({
	testCase: {
		type: Object,
		default: null
	}
})

const localTestCase = ref(props.testCase)

const closeModal = () => {
	emit('close')
}

const handleEditTest = () => {
	// emit('edit', localTestCase.value)
	closeModal()
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
	height: 90vh;
	overflow: scroll;
	background-color: white;
	padding: 20px;
	border-radius: 8px;
	box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.3); /* shadow effect */
}

.test-title {
	margin-bottom: 20px;
}

form {
	width: 800px; /* adjust width as needed */
}

label {
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

.actions-container {
	margin-bottom: 20px; /* Add margin between actions container and button */
}

.action {
	border: 1px solid #ccc;
	border-radius: 5px;
	padding: 10px;
	margin-bottom: 10px;
}

.action:last-child {
	margin-bottom: 0; /* Remove margin bottom for the last action */
}

.action label {
	font-weight: bold;
}

.expected-results input {
	margin-bottom: 5px; /* Add margin between expected results */
}

button {
	background-color: var(--crimson);
	color: white;
	border: none;
	padding: 10px 20px;
	cursor: pointer;
	width: 100%;
}

button:hover {
	background-color: #8a0057;
}
</style>
