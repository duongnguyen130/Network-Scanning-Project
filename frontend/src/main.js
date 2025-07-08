import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import './assets/tailwind.css'
import * as lucide from 'lucide-vue-next'

const app = createApp(App)
Object.entries(lucide).forEach(([name, component]) => {
  app.component(name, component)
})

createApp(App).use(router).mount('#app')

