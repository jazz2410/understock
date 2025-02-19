<script>
	import '../app.css';
	let { children } = $props();
	import Navbar from '$lib/Navbar.svelte';
</script>

<div class="bg-black min-h-screen text-white px-10">
<Navbar />
{@render children()}
</div>

