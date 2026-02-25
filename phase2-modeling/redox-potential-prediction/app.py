"""
app.py - Gradio Web Demo: 有机分子氧化还原电位预测
"""
import gradio as gr
from src.predict import predict_single


EXAMPLE_MOLECULES = [
    ["O=C1C=CC(=O)C=C1", "苯醌 (Benzoquinone)"],
    ["O=C1C=Cc2ccccc2C1=O", "蒽醌 (Anthraquinone)"],
    ["CCC(C#N)CC", "戊二腈衍生物"],
    ["c1ccc2c(c1)cc1ccc3cccc4ccc2c1c34", "芘 (Pyrene)"],
    ["CC(=O)Oc1ccccc1C(O)=O", "阿司匹林 (Aspirin)"],
    ["c1ccccc1", "苯 (Benzene)"],
]


def predict_ui(smiles: str) -> str:
    """Gradio 回调函数"""
    if not smiles or not smiles.strip():
        return "⚠️ 请输入有效的 SMILES 字符串"
    
    smiles = smiles.strip()
    result = predict_single(smiles)
    
    if result["error"]:
        return f"❌ 错误: {result['error']}"
    
    output = f"""✅ 预测结果

📝 输入 SMILES:     {result['smiles']}
🔬 标准 SMILES:     {result['canonical_smiles']}
⚡ 还原电位预测值:   {result['prediction']:.4f} V

📐 参考基准: vs. vacuum (乙腈溶剂, SMD 模型)

⚠️ 注意: 
- 此预测基于 DFT 计算数据训练的 XGBoost 模型
- 预测值是计算参考值，非实验实测值
- 模型在醌类等含氧有机分子上预测较为可靠
"""
    return output


def create_app():
    """创建 Gradio 界面"""
    demo = gr.Interface(
        fn=predict_ui,
        inputs=gr.Textbox(
            label="Input SMILES",
            placeholder="e.g. O=C1C=CC(=O)C=C1 (Benzoquinone)",
            lines=1,
        ),
        outputs=gr.Textbox(
            label="Prediction Result",
            lines=12,
        ),
        title="Organic Molecule Redox Potential Predictor",
        description="Based on OMEAD dataset (26,218 molecules) + XGBoost. Input a SMILES string to predict reduction potential.",
        examples=[[e[0]] for e in EXAMPLE_MOLECULES],
    )
    return demo


if __name__ == "__main__":
    # 预加载模型，避免首次请求慢
    from src.predict import load_model
    load_model()
    
    app = create_app()
    app.launch(server_name="127.0.0.1", server_port=7860)
