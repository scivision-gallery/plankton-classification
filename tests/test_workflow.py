import pytest
import os

os.environ['KMP_DUPLICATE_LIB_OK']='True'

def test_workflow():
    from scivision import default_catalog, load_pretrained_model, load_dataset

    model_name = 'resnet50-plantkton'
    compatible_datasources = default_catalog.compatible_datasources(model_name).to_dataframe()

    models = default_catalog.models.to_dataframe()
    targetmodel = models[models.name == model_name].url.item()
    model = load_pretrained_model(targetmodel, allow_install=True)

    target_datasource = compatible_datasources.loc[compatible_datasources['name'] == 'data-004']
    cat = load_dataset(target_datasource.url.item())
    dataset = cat.plankton().to_dask()

    model.predict(dataset, batch_size=26)
