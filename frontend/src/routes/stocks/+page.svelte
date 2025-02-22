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

	let items = [];

    onMount(async () => {
        try {
            const response = await fetch('http://localhost:8000/stocks');
	    // const response = await fetch('/api/stocks');
            items = await response.json();
			console.log(items);
        } catch (error) {
            console.error('Error fetching stocks:', error);
        }
    });

</script>




<div class="item-center flex justify-center">
	{#if items.length}
	<Table
		{items}
        striped={true}
		placeholder="Search by ticker or stock name"
		hoverable={true}
		filter={(item, searchTerm) => item.ticker.toLowerCase().includes(searchTerm.toLowerCase())
                                   || item.stockName.toLowerCase().includes(searchTerm.toLowerCase())                        }
        class="rounded-2xl"
	>
	
		<TableHead>
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
					<a href={`/stock/${item.ticker}`} class="font-medium text-primary-600 hover:underline dark:text-primary-500">Display valuation</a>
				  </TableBodyCell>
			</TableBodyRow>
		</TableBody>
	</Table>
	{:else}
	<p>Loading data...</p>
	{/if}
</div>
