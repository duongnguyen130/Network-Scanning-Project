<template>
  <div>
    <h2 class="text-2xl font-bold mb-4">Hosts Discovery Results</h2>
    <button @click="runPingScan" class="mb-4 bg-blue-600 text-white px-4 py-2 rounded">Discover</button>
    <table class="w-full table-auto bg-white shadow rounded">
      <thead>
        <tr>
          <th class="p-2">IP Address</th>
          <th class="p-2">OS</th>
          <th class="p-2">Device Type</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="host in pingResults" :key="host.host">
          <td class="p-2">{{ host.host }}</td>
          <td class="p-2">{{ host.OS }}</td>
          <td class="p-2">{{ host["Device Type"] }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'

const pingResults = ref([])

const runPingScan = async () => {
  try {
    const response = await axios.get('/api/ping-scan/')
    pingResults.value = response.data.hosts || []
  } catch (err) {
    console.error(err)
  }
}
</script>