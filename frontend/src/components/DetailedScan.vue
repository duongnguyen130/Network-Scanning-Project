<template>
  <div>
    <h2 class="text-2xl font-bold mb-4">Devices Discovery Results</h2>
    <button @click="runDetailedScan" class="mb-4 bg-blue-600 text-white px-4 py-2 rounded"> Discovery </button>
    <table class="w-full table-auto bg-white shadow rounded">
      <thead>
        <tr>
          <th class="p-2">IP Address</th>
          <th class="p-2">OS</th>
          <th class="p-2">Device Type</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="host in detailedResults" :key="host.host">
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

const detailedResults = ref([])

const runDetailedScan = async () => {
  try {
    const response = await axios.get('/api/detailed-scan/')
    detailedResults.value = response.data.hosts || []
  } catch (err) {
    console.error(err)
  }
}
</script>