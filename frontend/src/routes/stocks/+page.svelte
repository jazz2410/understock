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
	<p class="text-center">Click on the ticker symbol to see the evaluation</p>
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
		</TableHead>
		<TableBody tableBodyClass="divide-y">
			<TableBodyRow slot="row" let:item>
				
				<TableBodyCell>
					<button on:click={() => goto(`/stock/${item.ticker}`)} class="w-20 h-10 cursor-pointer hover:bg-orange-400">
						{item.ticker}
					</button>
				</TableBodyCell>

				<TableBodyCell>
					<button on:click={() => goto(`/stock/${item.ticker}`)} class="cursor-pointer w-full h-10 hover:bg-orange-400">
						{item.stockName}
					</button>
				</TableBodyCell>
                <TableBodyCell>{item.lastPrice}</TableBodyCell>
                <TableBodyCell>{item.fairValueShare}</TableBodyCell>
                <TableBodyCell>{item.delta}</TableBodyCell>
			</TableBodyRow>
		</TableBody>
	</Table>
	{:else}
	<p>Loading data...</p>
	{/if}
</div>
</div>

<Footer></Footer>