<template>
  <div class="bg-white shadow rounded-lg p-6 space-y-6">
    <div class="flex space-x-4">
      <button @click="runPingScan" class="px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700">
        Run Ping Scan
      </button>
      <button @click="runDetailedScan" class="px-4 py-2 bg-green-600 text-white rounded hover:bg-green-700">
        Run Detailed Scan
      </button>
    </div>

    <div v-if="loading" class="text-gray-600">⏳ Scanning...</div>

    <div v-if="pingResults.length">
      <h3 class="text-xl font-medium mt-6">Ping Scan Results</h3>
      <ul class="list-disc pl-6">
        <li v-for="host in pingResults" :key="host.host">{{ host.host }}</li>
      </ul>
    </div>

    <div v-if="detailedResults.length">
      <h3 class="text-xl font-medium mt-6">Detailed Scan Results</h3>
      <ul class="list-disc pl-6">
        <li v-for="host in detailedResults" :key="host.host">
          {{ host.host }} - {{ host.OS }} - {{ host['Device Type'] }}
        </li>
      </ul>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'

const pingResults = ref([])
const detailedResults = ref([])
const loading = ref(false)

const runPingScan = async () => {
  loading.value = true
  try {
    const response = await axios.get('/api/ping-scan/')
    pingResults.value = response.data.hosts || []
  } catch (err) {
    console.error('Ping Scan Error:', err)
  } finally {
    loading.value = false
  }
}

const runDetailedScan = async () => {
  loading.value = true
  try {
    const response = await axios.get('/api/detailed-scan/')
    detailedResults.value = response.data.hosts || []
  } catch (err) {
    console.error('Detailed Scan Error:', err)
  } finally {
    loading.value = false
  }
}
</script>
