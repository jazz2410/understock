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
</script>
<div class="bg-black min-h-screen text-white">
<div class="py-5 px-25">
    <nav class="text-white shadow-md py-3">
        <div class="container mx-auto flex justify-between items-center px-6">
            
            <!-- Left Spacer (Keeps Centered Title in Place) -->
            <div class="w-1/3"></div>

            <!-- Website Name (Centered) -->
            <div class="w-1/3 text-center text-xl font-bold">
                <a href="/" class="hover:text-blue-500 underline">Understocks</a>
            </div>

            <!-- Right Menu -->
            <div class="w-1/3 flex justify-end space-x-6 text-lg font-medium">
                <a href="/" class="hover:text-blue-500">Services</a>
                <a href="/" class="hover:text-blue-500">Contact</a>
            </div>

        </div>
    </nav>
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
			<TableHeadCell sort={(a, b) => a.ticker.localeCompare(b.ticker)} defaultSort>Ticker</TableHeadCell>
			<TableHeadCell>Stock name</TableHeadCell>
            <TableHeadCell>Last price in USD</TableHeadCell>
            <TableHeadCell>Fair value (DCF)</TableHeadCell>
            <TableHeadCell sort={(a, b) => a.delta - b.delta} defaultDirection="desc">Delta</TableHeadCell>
		</TableHead>
		<TableBody tableBodyClass="divide-y">
			<TableBodyRow slot="row" let:item>
				<TableBodyCell>{item.ticker}</TableBodyCell>
				<TableBodyCell>{item.stockName}</TableBodyCell>
                <TableBodyCell>{item.lastPrice}</TableBodyCell>
                <TableBodyCell>{item.fairValue}</TableBodyCell>
                <TableBodyCell >{item.delta}</TableBodyCell>
			</TableBodyRow>
		</TableBody>
	</Table>
</div>
</div>