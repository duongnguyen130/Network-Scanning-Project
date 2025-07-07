<template>
  <div>
    <button @click="runPingScan">Run Ping Scan</button>
    <button @click="runDetailedScan">Run Detailed Scan</button>

    <div v-if="loading">⏳ Loading...</div>

    <div v-if="pingResults.length">
      <h2>Ping Scan Results:</h2>
      <ul>
        <li v-for="host in pingResults" :key="host.host">{{ host.host }}</li>
      </ul>
    </div>

    <div v-if="detailedResults.length">
      <h2>Detailed Scan Results:</h2>
      <ul>
        <li v-for="host in detailedResults" :key="host.host">
          {{ host.host }} - {{ host.OS }} - {{ host["Device Type"] }}
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
