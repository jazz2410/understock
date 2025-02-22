export async function load({ fetch }) {
	const response = await fetch('/api/stocks'); // Replace with your FastAPI URL
	const data = await response.json();
        console.log(data);
	return { data };
}
