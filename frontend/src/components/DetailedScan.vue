<template>
  <div>
    <h2>Detailed Scan Results</h2>
    <ul>
      <li v-for="host in results" :key="host.host">
        {{ host.host }} - {{ host.OS }} - {{ host['Device Type'] }}
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const results = ref([])

onMounted(async () => {
  const res = await axios.get('/api/detailed-scan/')
  results.value = res.data.hosts || []
})
</script>
