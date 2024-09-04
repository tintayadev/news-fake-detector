<!-- src/routes/+page.svelte -->
<script>
    import { onMount } from 'svelte';
    import axios from 'axios';

    let newsText = '';
    let result = '';

    async function predictNews() {
        try {
            const response = await axios.post('http://127.0.0.1:8000/predict/', {
                text: newsText
            });
            result = response.data.result;
        } catch (error) {
            console.error('Error predicting news:', error);
            result = 'Error predicting news';
        }
    }
</script>

<style>
    body {
        font-family: Arial, sans-serif;
        background-color: #f4f4f4;
        margin: 0;
        padding: 0;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
    }
    .container {
        background: white;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        width: 100%;
        max-width: 600px;
        box-sizing: border-box;
    }
    textarea {
        width: 100%;
        height: 150px;
        margin-bottom: 10px;
        padding: 10px;
        border-radius: 4px;
        border: 1px solid #ddd;
    }
    button {
        background-color: #007bff;
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 4px;
        cursor: pointer;
    }
    button:hover {
        background-color: #0056b3;
    }
    .result {
        margin-top: 20px;
        font-size: 1.2em;
        font-weight: bold;
    }
</style>

<div class="container">
    <h1>Fake News Detector</h1>
    <textarea bind:value={newsText} placeholder="Enter news text here..."></textarea>
    <button on:click={predictNews}>Predict</button>
    {#if result}
        <div class="result">Result: {result}</div>
    {/if}
</div>
