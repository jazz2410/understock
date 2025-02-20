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

	export let data;
	const items = data.data;
	console.log(items[0].timestamp)
</script>
<div class="flex ml-25">
<p class="font-light">Data updated: {items[0].timestamp}</p>
</div>
<div class="item-center flex justify-center">
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
			<TableHeadCell sort={(a, b) => a.ticker.localeCompare(b.ticker)} defaultSort>TICKER</TableHeadCell>
			<TableHeadCell>Stock name</TableHeadCell>
            <TableHeadCell>Last price [USD]</TableHeadCell>
            <TableHeadCell>Fair value [USD] (DCF)</TableHeadCell>
            <TableHeadCell sort={(a, b) => a.delta - b.delta} defaultDirection="desc">DELTA [%] (DCF)</TableHeadCell>
		    <TableHeadCell>Action</TableHeadCell>
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
</div>
