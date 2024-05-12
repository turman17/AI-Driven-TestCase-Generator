export default interface TestCase {
	testCaseId: string
	title: string
	description: string
	preConditions: string[]
	requirement: string[]
	actions: { "step": string, "expectedResults": string[] }[]
}