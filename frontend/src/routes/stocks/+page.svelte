<script lang="js">
	import { onMount } from 'svelte';
	import {
		Table,
		TableBody,
		TableBodyCell,
		TableBodyRow,
		TableHead,
		TableHeadCell,
		Checkbox,
		TableSearch
	} from 'flowbite-svelte';
	import { goto } from '$app/navigation';
	import Footer from '$lib/Footer.svelte';
	let items = [];

    onMount(async () => {
        try {
    	  //const response = await fetch('http://localhost:8000/stocks');
	    	const response = await fetch('/api/stocks');
            items = await response.json();
			console.log(items);
        } catch (error) {
            console.error('Error fetching stocks:', error);
        }
    });

</script>

<div class="items-center flex justify-center">
	<div class="w-full max-w-6xl overflow-x-auto">
	{#if items.length}
	<p class="mb-4 text-sm text-gray-400 text-center">📅 Table was updated on {items[0].timestamp}</p>
	<Table
		{items}
        striped={true}
		placeholder="Search by ticker or stock name"
		hoverable={true}
		filter={(item, searchTerm) => item.ticker.toLowerCase().includes(searchTerm.toLowerCase())
                                   || item.stockName.toLowerCase().includes(searchTerm.toLowerCase())                        }
        class="rounded-2xl"
	>
	
		<TableHead class="rounded-t-2xl">
			<TableHeadCell class="text-white" sort={(a, b) => a.ticker.localeCompare(b.ticker)} defaultSort>TICKER</TableHeadCell>
			<TableHeadCell class="text-white">Stock name</TableHeadCell>
            <TableHeadCell class="text-white">Last price [USD]</TableHeadCell>
            <TableHeadCell class="text-white">Fair value [USD] (DCF)</TableHeadCell>
            <TableHeadCell class="text-white" sort={(a, b) => a.delta - b.delta} defaultDirection="desc">DELTA [%] (DCF)</TableHeadCell>
		    <TableHeadCell class="text-white">Action</TableHeadCell>
		</TableHead>
		<TableBody tableBodyClass="divide-y">
			<TableBodyRow slot="row" let:item>
				<TableBodyCell>{item.ticker}</TableBodyCell>
				<TableBodyCell>{item.stockName}</TableBodyCell>
                <TableBodyCell>{item.lastPrice}</TableBodyCell>
                <TableBodyCell>{item.fairValueShare}</TableBodyCell>
                <TableBodyCell>{item.delta}</TableBodyCell>
				<TableBodyCell>
					<button on:click={() => goto(`/stock/${item.ticker}`)} class="px-1 py-1 my-1 rounded-lg bg-orange-500 hover:bg-orange-600 text-black font-semibold shadow-md 
               transition duration-300 ease-in-out transform hover:scale-105 focus:outline-none focus:ring-2 
               focus:ring-orange-400 dark:text-white">See evaluation</button>
				</TableBodyCell>
			</TableBodyRow>
		</TableBody>
	</Table>
	{:else}
	<p>Loading data...</p>
	{/if}
</div>
</div>

<Footer></Footer>