# Data Virtualisation

Data Virtualisation is a key component in the reference architecture. It needs to provide the following capabilities:-

1. Pull/push datasets from different persistant data store types (files, queues, relational databases, data lakes etc)
2. Expose the datasets as sql accessible views
3. Integrate with an organisation's authentication system
4. Apply user authorisation policies against the sql accessible views
5. Provide odbc, jdbc and API access to the datasets
6. Convert datasets to different formats e.g. CSV, JSON, XML, HTML

From a data mesh/data product perspective, Data Virtualisation covers the need for:-
1. Datasets to be globally addressable in a standardised way
2. Dataset user authorisation policies to be uniformally implemented for different data product types.
3. Polyglot (i.e. multi-format)