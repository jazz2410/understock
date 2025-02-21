export async function load({ fetch }) {
	const response = await fetch('http://localhost:8000/stocks'); // Replace with your FastAPI URL
	const data = await response.json();
	return { data };
}
